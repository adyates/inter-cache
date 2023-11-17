# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# From Codebunk

'''
PART 1: Astranis sends down telemetry in a special JSON structure. This JSON
has been deserialized for you into a dictionary that is ready to be processed.
They are received on the ground meeting the following constraints
* Keys are always strings
* Values may be floats, integers, strings, or dictionaries

The first stage of processing a telemetry packet is to flatten it. Please
implement a packet flattener with the following signature that unpacks any
hierarchy in the original dict and makes new keys that are dot delimited to
represent the original chain of keys to the value.

def flatten_packet(packet: dict) -> dict:
    ...

This function takes in the raw packet and returns a dictionary representing the
flattened form. As an example, if you were given the following packet

packet = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': {'f': 4}, 'g': 5}}

we would expect the output to be
{'a': 1, 'b': 2, 'c.d': 3, 'c.e.f': 4, 'c.g': 5}

===
PART 2: With packets flattened, we are now ready to start storing the data in a
time series manner. Normally, we would do this in a database, but we'll store
the history internal to our class for the purposes of this interview. For this
part, implement a class that ingests raw packets.

The class should have the following structure

    class PacketMonitor:
        def __init__(self, alert_config: dict):
            pass

        def monitor(self, packet: dict) -> None:
            pass

        def results(self) -> None:
            pass

It is instantiated an alert configuration object that will be used for the
future part. That may be ignored for now. PacketMonitor.monitor() is the focus
for now and is responsible for analyzing one packet at a time. For each packet,
this method should flatten the message and retain a history of all point values
associated with the flatform key along with the time that the message was
processed. PacketMonitor.results() should, when called, display all of the
flatform keys observed along with the number of points for each key that have
been ingested.


{
  'c.e.f': [(4 , utc.now()), (12, utc.now() + 12) ]


}
===

PART 3: Modify PacketMonitor such that it uses the input configuration dict to
alert on important value changes. This implementation should be stateful in
that we alert only on transitions into and out of the acceptable telemetry
ranges. The config should support optionally configuring a min, max, or both
for a named telemetry point. An example config may look like the following:

    ALERT_CONFIG = {
        'POWER.BATTERIES.BATT1.VOLTAGE': {'min': 24.5, 'max': 27.5},
        'POWER.BATTERIES.BATT2.CURRENT': {'max': 3.9},
        'GNC.MODE': {'min': 0}
    }

Lastly, modify results() to show a tally of state transitions (e.g. OK->OUTSIDE
MAX: 10) by telemetry point as well as the current state of all telemetry
points at the time results() is called.

'''

# from datetime import datetime
import time

class PacketMonitor:
    
        def __init__(self, alert_config: dict):
            self.alert_config = alert_config
            self._alert_states = {}
            self._alert_history = {}
            self._key_history = {}        

        def _check_alerts(self, key, value, timestamp):
            # Check the new value against alowable ranges
            valueState = ''
            if (key in self.alert_config) :
                # We have configured something
                config = self.alert_config[key]
                if ('min' in config and value < config['min']):
                    # Outside the lower bound
                    valueState = 'OUTSIDE'
                elif ('max' in config and value > config['max']):
                    # outside upper bound
                    valueState = 'OUTSIDE'
                else: 
                    valueState = 'OK'
            
            if self._alert_states.get(key, '') != valueState:
                # Update history
                state_history = self._alert_history.get(key, [])
                state_history.append((valueState, timestamp))
                self._alert_history[key] = state_history
                                     
                # Update current state
                self._alert_states[key] = valueState            
            
        def _append_history(self, key, value, timestamp):
            history = self._key_history.get(key, [])
            history.append((value, timestamp))
            self._key_history[key] = history                       
                       
        def monitor(self, packet):
            processing_time = time.time()
            
            def _flatten_packet(packet, prefix, result):    
                for key, value in packet.items():
                    use_key = prefix+key
                    if isinstance(value, dict):
                        _flatten_packet(value, use_key + '.', result)
                    else:
                        self._append_history(use_key, value, processing_time)
                        self._check_alerts(use_key, value, processing_time)
            _flatten_packet(packet, '', {})

        def results(self):
            for key, value in self._key_history.items():
                print(key, value, len(value))
            print(self._alert_states)
            print(self._alert_history)
        

packet =  {'a': 1, 'b': 2, 'c': {'d': 3, 'e': {'f': 4}, 'g': 5}}
packet2 = {'a': 11, 'b': 22, 'c': {'d': 33, 'e': {'x': 44}}}
pm = PacketMonitor({'c.d': {'min': 1, 'max': 11}})

pm.monitor(packet)
pm.monitor({})
pm.monitor(packet2)
pm.results()

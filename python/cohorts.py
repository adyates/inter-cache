'''
There are n vehicles traveling to a common endpoint along a single-lane route. The endpoint is target miles distant.

You have two integer arrays, position and speed, both of equal length n, where position[i] signifies the location of the ith vehicle and speed[i] symbolizes the speed of the ith vehicle (measured in miles per hour).

A vehicle cannot overtake another vehicle in front of it, but it can match its speed and drive right behind it. The quicker vehicle will reduce its speed to align with the slower vehicle's speed. The gap between these two vehicles is overlooked (i.e., they are assumed to be at the same location).

A vehicle cohort refers to a group of vehicles moving at the same speed and location. Note that a single vehicle can also constitute a vehicle cohort.

If a vehicle reaches a vehicle cohort right at the endpoint, it is still counted as one vehicle cohort.

The task is to calculate the number of vehicle cohorts that will reach the endpoint.

target = 100, position = [0,2,4], speed = [4,2,1]
'''
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

target = 100
position = [0,2,4]
speed = [4,2,1]

target = 100
position = [50,25,10]
speed = [10,10, 50]


class Cohort(object):

    def __init__(self, vehicle, position, speed):
        self.vehicles = [vehicle]
        self.position = position
        self.speed = speed

cohorts = []
for item in range(0, len(position)):
    cohorts.append(Cohort(item, position[item], speed[item]))

def computeCohorts(cohorts):
    # Sort in ascending position order
    sortedCohorts = sorted(cohorts, key=lambda x: x.position, reverse=True)

    finalCohorts = []

    while(sortedCohorts):
        # Advance all cohorts
        for c in sortedCohorts:
            c.position += c.speed


        # Check ordering and combine
        index = 0
        while (index < len(sortedCohorts) -1):
            current = sortedCohorts[index]
            next =  sortedCohorts[index + 1]
            if current.position <= next.position:
                # Compress cohorts, compare current to the one after
                current.vehicles.extend(next.vehicles)
                current.speed = min(current.speed, next.speed)
                sortedCohorts.pop(index+1)
            else:
                # Move on to the next vehicle cohort
                index += 1

        # Check if any cohorts are done
        index = 0
        while (index < len(sortedCohorts)):
            if sortedCohorts[index].position >= target:
                # Add this cohort to the final list so we don't combine it again
                finalCohorts.append(sortedCohorts.pop(index))
            else:
                # Check the next vehicle cohort
                index += 1

    return finalCohorts
    

newC = computeCohorts(cohorts)


def printCohorts(cohorts):
    for c in cohorts:
        print(c.vehicles, c.position, c.speed)

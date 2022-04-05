import csv
import random

# This method extracts data from the Compound exercise csv and returns list of dictionaries
# of the three different workouts
def CompoundWorkout():
    CompoundPushDict = {}
    CompoundPullDict = {}
    CompoundLegDict = {}
    with open('Compound Exercises.csv', newline='\n') as file:
        reader = csv.reader(file)
        for line in reader:
            WorkoutName = line[0]
            WorkoutType = line[2]
            line.pop(0)
            if WorkoutType == "Leg":
                CompoundLegDict[WorkoutName] = line
            if WorkoutType == "Push":
                CompoundPushDict[WorkoutName] = line
            if WorkoutType == "Pull":
                CompoundPullDict[WorkoutName] = line
    CompoundWorkoutList = [CompoundLegDict, CompoundPullDict, CompoundPushDict]
    return CompoundWorkoutList
# This method is the same as above except this extracts data from the Isolation exercise csv
def IsolationWorkout():
    IsolationPushDict = {}
    IsolationPullDict = {}
    IsolationLegDict = {}
    with open('Isolation Exercises.csv', newline='\n') as file:
        reader = csv.reader(file)
        for line in reader:
            WorkoutName = line[0]
            WorkoutType = line[2]
            line.pop(0)
            if WorkoutType == "Leg":
                IsolationLegDict[WorkoutName] = line
            if WorkoutType == "Push":
                IsolationPushDict[WorkoutName] = line
            if WorkoutType == "Pull":
                IsolationPullDict[WorkoutName] = line
    IsoWorkoutList = [IsolationLegDict, IsolationPullDict, IsolationPushDict]
    return IsoWorkoutList

# This is a 2D Matrix I created to represent the Graph of the order of the workout
Graph = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0]
]
# I created this list and assigned each index false to help keep track for each node that I visited
visited = [False for eachVertex in range(len(Graph))]
TopSortOutput = []  # This List will contain the Output from the Topological Sort method


def Topological_Sort_Helper(node):
    visited[node] = True  # Each time I visit a node, I mark it true
    for edge in Graph[node]:  # Then I find the edge from one node to the other
        if not visited[edge]:  # If I haven't visited the vertex adjacent to the node
            Topological_Sort_Helper(edge)  # Then I make a recursive call and now start on the next node
    TopSortOutput.append(node)  # I add the nodes (vertexes) in this list in the order in which I have "discovered" the vertex
    return TopSortOutput


def Topological_Sort():
    for nodes in range(len(Graph)):  # Traverse through the Graph
        if not visited[nodes]:  # Then If I haven't visited the nodes
            Topological_Sort_Helper(nodes)  # I make a recursive call to the helper to discover the
    TopSortOutput.reverse()  # Then to produce a topological sort, I reverse the list
    return TopSortOutput
# This is a method to generate a recovery workout
def recover():
    num = random.randint(0, 1)
    if num == 0:
        return "Stretch for 10 to 15 minutes"
    if num == 1:
        return "Do an ab circuit for 8 to 10 minutes"

# This is a method to generate a warm-up
def warmUp():
    number = random.randint(0, 2)
    if number == 0:
        print("Warm-up:\nStretch for 5 minutes and then a 10 minute Jog")
    elif number == 1:
        print("Warm-up:\nStretch for 5 minutes and then 10 minutes on a Stationary Bike ")
    else:
        print("Warm-up:\nStretch for 5 minutes and then a 5 minute Jog")
# The folowing methods: legWorkout, pullWorkout, and pushWorkout, all use the result from
# the topological sort method to produce a list of the workout in order
def legWorkout():
    legdict = CompoundWorkout()[0]
    compoundName = list(legdict.keys())
    legIsolationDict = IsolationWorkout()[0]
    isoName = list(legIsolationDict.keys())
    extra = list(legdict.values())
    isoExtra = list(legIsolationDict.values())
    legIso1 = []
    legIso2 = []
    legCom3 = []
    legCom4 = []
    legCom5 = []
    for count, more in enumerate(extra):
        for zoom in more:
            if zoom == '3':
                legCom3.append(compoundName[count])
            if zoom == '4':
                legCom4.append(compoundName[count])
            if zoom == '5':
                legCom5.append(compoundName[count])
    for counter, val in enumerate(isoExtra):
        for value in val:
            if value == '1':
                legIso1.append(isoName[counter])
            if value == '2':
                legIso2.append(isoName[counter])
    rand1 = random.randint(0, 1)
    rand2 = random.randint(0, 2)
    finalWorkout = []
    for num in Topological_Sort():
        if num == 5:
            finalWorkout.insert(0, legCom5[rand1])
        elif num == 4:
            finalWorkout.insert(1, legCom4[rand2])
        elif num == 3:
            finalWorkout.insert(2, legCom3[rand1])
        elif num == 2:
            finalWorkout.insert(3, legIso2[rand1])
        elif num == 1:
            finalWorkout.insert(4, legIso1[rand2])
        else:
            finalWorkout.insert(5, recover())
    return finalWorkout

def pullWorkout():
    pullComDict = CompoundWorkout()[1]
    pullIsoDict = IsolationWorkout()[1]
    pullComName = list(pullComDict.keys())
    pullIsoName = list(pullIsoDict.keys())
    pullComExtra = list(pullComDict.values())
    pullIsoExtra = list(pullIsoDict.values())
    pull5 = []
    pull4 = []
    pull3 = []
    pull2 = []
    pul11 = []
    for count, values in enumerate(pullComExtra):
        for val in values:
            if val == '5':
                pull5.append(pullComName[count])
            if val == '4':
                pull4.append(pullComName[count])
            if val == '3':
                pull3.append(pullComName[count])
    for counter, val in enumerate(pullIsoExtra):
        for value in val:
            if value == '2':
                pull2.append(pullIsoName[counter])
            if value == '1':
                pul11.append(pullIsoName[counter])
    rand1 = random.randint(0, 1)
    rand2 = random.randint(0, 2)
    rand3 = random.randint(0, 4)
    rand4 = random.randint(0, 5)
    FinalPullWorkout = []
    for num in Topological_Sort():
        if num == 5:
            FinalPullWorkout.insert(0, pull5[rand1])
        elif num == 4:
            FinalPullWorkout.insert(1, pull4[rand1])
        elif num == 3:
            FinalPullWorkout.insert(2, pull3[rand2])
        elif num == 2:
            FinalPullWorkout.insert(3, pull2[rand3])
        elif num == 1:
            FinalPullWorkout.insert(4, pul11[rand4])
        else:
            FinalPullWorkout.insert(5, recover())
    return FinalPullWorkout

def pushWorkout():
    pushComDict = CompoundWorkout()[2]
    pushIsoDict = IsolationWorkout()[2]
    pushComName = list(pushComDict.keys())
    pushIsoName = list(pushIsoDict.keys())
    pushComExtra = list(pushComDict.values())
    pushIsoExtra = list(pushIsoDict.values())
    push5 = []
    push4 = []
    push3 = []
    push2 = []
    push1 = []
    for count, values in enumerate(pushComExtra):
        for val in values:
            if val == '5':
                push5.append(pushComName[count])
            if val == '4':
                push4.append(pushComName[count])
            if val == '3':
                push3.append(pushComName[count])
    for counter, info in enumerate(pushIsoExtra):
        for value in info:
            if value == '2':
                push2.append(pushIsoName[counter])
            if value == '1':
                push1.append(pushIsoName[counter])
    rand1 = random.randint(0, 3)
    rand2 = random.randint(0, 4)
    rand3 = random.randint(0, 5)
    FinalPushWorkout = []
    for num in Topological_Sort():
        if num == 5:
            FinalPushWorkout.insert(0, push5[rand1])
        elif num == 4:
            FinalPushWorkout.insert(1, push4[rand1])
        elif num == 3:
            FinalPushWorkout.insert(2, push3[rand2])
        elif num == 2:
            FinalPushWorkout.insert(3, push2[rand3])
        elif num == 1:
            FinalPushWorkout.insert(4, push1[rand3])
        else:
            FinalPushWorkout.insert(5, recover())
    return FinalPushWorkout

# Here in the main is where I prompt the user to enter what type of workout they want to do
# and depending on the workout they choose, I then call specific workout method
# and display the workout
def main():
    str = input("What type of workout would you like to do:\nLegs, Push, Pull:")
    fixInput = str.lower()
    if fixInput == "legs":
        warmUp()
        print("Workout: ")
        workout = legWorkout()
        for compoundExercise in range(0, 3):
            print("4 sets of 6 reps of " + workout[compoundExercise] + "\n")
        for isolationExercise in range(3, 5):
            print("3 sets of 10 reps of " + workout[isolationExercise] + "\n")
        print("Recovery:\n" + workout[5])
    elif fixInput == "pull":
        warmUp()
        print("Workout: ")
        workout = pullWorkout()
        for comPull in range(0, 3):
            print("4 sets of 10 reps of " + workout[comPull] + "\n")
        for isoPull in range(3, 5):
            print("3 sets of 10 reps of " + workout[isoPull] + "\n")
        print("Recovery:\n" + workout[5])
    else:
        warmUp()
        print("Workout: ")
        workout = pushWorkout()
        for comPush in range(0, 3):
            print("3 sets of 12 reps of " + workout[comPush] + "\n")
        for isoPush in range(3, 5):
            print("3 sets of 10 reps of " + workout[isoPush] + "\n")
        print("Recovery:\n" + workout[5])


if __name__ == '__main__':
    main()
# My goal for this project was to show how Discrete Mathematics
# more specifically Recursion and Graph Theory
# can be used in everyday life and how something like a
# Gym workout plan can be created by using those topics
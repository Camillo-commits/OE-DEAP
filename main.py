import numpy
import numpy as np
from deap import tools
from mealpy.swarm_based.SSO import BaseSSO

from SVC.functionallity import solve, mutationSVC, mutationSVCWithSelection, SVCParametersFitness, \
    SVCParametersFeatureFitness, SVCparameters, SVCParametersFeatures, __kernel__
from binary.binary_representation import solve_binary_representation
from real.fitness import get_fitness, get_fitness2
from real.real_representation import solve_real_representation
import matplotlib.pyplot as plt
from utils import plot3d, plotStdAvg
import pandas as pd
from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

pd.set_option('display.max_columns', None)
df = pd.read_csv("resources/heart_failure_clinical_records_dataset.csv")

y = df['DEATH_EVENT']
df.drop('DEATH_EVENT', axis=1, inplace=True)
numberOfAttributes = len(df.columns)
print('Count of our attributes ', numberOfAttributes)

mms = MinMaxScaler()
df_norm = mms.fit_transform(df)
clf = SVC()
scores = model_selection.cross_val_score(clf, df_norm, y,
                                         cv=5, scoring='accuracy', n_jobs=-1)
print('Our model accuracy: ', scores.mean())

#is_min = True
#selector = tools.selTournament
#crosser = tools.cxOnePoint
#mutator = tools.mutShuffleIndexes
#size_of_population = 10
#probability_mutation = 0.3
#probability_crossover = 0.5
#number_iteration = 100
#number_elitism = 1
#x1, x2, y, std, avg = solve_binary_representation(is_min, selector, crosser, mutator, size_of_population,
#                                                  probability_mutation, probability_crossover,
#                                                  number_iteration, number_elitism)
#print("Done!")
#plot3d(x1, x2, y, colorbar=True)
#plotStdAvg(std, avg)

is_min = True
selector = tools.selTournament
crosser = tools.cxBlend
mutator = tools.mutGaussian
size_of_population = 10
probability_mutation = 0.3
probability_crossover = 0
number_iteration = 100
number_elitism = 1
#listKernel = ["linear", "rbf", "poly", "sigmoid"]

# __kernel__ = "abc"
# x1, x2, y, std, avg = solve(is_min, selector, crosser, mutationSVC, size_of_population,
#                                                 probability_mutation,
#                                                 probability_crossover, number_iteration, number_elitism, numberOfAttributes, y, df, SVCParametersFitness, SVCparameters, "linear")
# print("Done!")
#
# x1, x2, y, std, avg = solve(is_min, selector, crosser, mutationSVCWithSelection, size_of_population,
#                                                 probability_mutation,
#                                                 probability_crossover, number_iteration, number_elitism, numberOfAttributes, y, df, SVCParametersFeatureFitness, SVCParametersFeatures, "abc")
# print("Done!")
#


problem_dict1 = {

    "fit_func": get_fitness2,

    "lb": [-10],

    "ub": [10],

    "minmax": "min",

    "n_dims": 3,
}

epoch = 1000

pop_size = 50

model = BaseSSO(problem_dict1, epoch, pop_size)

best_position, best_fitness = model.solve()

print(f"Solution: {best_position}, Fitness: {best_fitness}")
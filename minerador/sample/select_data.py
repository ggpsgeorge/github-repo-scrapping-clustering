from view_model import ViewModel

# 1 - Initialising things ===================================================

#############
# IMPORTANT #
#############
token = ""
#############
# IMPORTANT #
#############

viewRepository = ViewModel(token)

# 2 - Getting data

numberOfRepositories = viewRepository.getTotalNumberOfRepositories()
print("Total Number of Repositories: ")
print(numberOfRepositories)

numberOfFeatures = viewRepository.getTotalNumberOfFeatures()
print("Total Number of Features: ")
print(numberOfFeatures)

numberOfScenarios = viewRepository.getTotalNumberOfScenarios()
print("Total Number of Scenarios: ")
print(numberOfScenarios)

numberOfSteps = viewRepository.getTotalNumberOfSteps()
print("Total Number of Steps: ")
print(numberOfSteps)

numberOfReposThatContainFeature = viewRepository.getNumberOfReposThatContainFeature()
print("Number Of Repos That Contain Feature: ")
print(numberOfReposThatContainFeature)

languages = viewRepository.getNumberOfReposPerLanguages()
print(languages)

countries = viewRepository.getNumberOfReposPerCountry()
print(countries)

scenariosPerRepo = viewRepository.getNumberOfScenariosPerRepo()
print("Number os Scenarios per Repository:")
print(scenariosPerRepo)

scenariosPerFeature = viewRepository.getNumberOfScenariosPerFeature()
print("Number os Scenarios per Feature:")
print(scenariosPerFeature)

# ===============================================================================================
averageFeaturesPerRepository = viewRepository.getAverageNumberOfFeaturesPerRepository()
print("Average Number of Features per Repository:")
print(averageFeaturesPerRepository)

averageScenariosPerRepository = viewRepository.getAverageNumberOfScenariosPerRepository()
print("Average Number of Scenarios per Repository:")
print(averageScenariosPerRepository)

averageStepsPerRepository = viewRepository.getAverageNumberOfStepsPerRepository()
print("Average Number of Steps per Repository:")
print(averageStepsPerRepository)

averageScenariosPerFeature = viewRepository.getAverageNumberOfScenariosPerFeature()
print("Average Number of Scenarios per Feature:")
print(averageScenariosPerFeature)

averageStepsPerFeature = viewRepository.getAverageNumberOfStepsPerFeature()
print("Average Number os Steps per Feature:")
print(averageStepsPerFeature)

averageStepsPerScenario = viewRepository.getAverageNumberOfStepsPerScenario()
print("Average Number os Steps per Scenario:")
print(averageStepsPerScenario)

# ===============================================================================================
averageSizeOfRepositories = viewRepository.getAverageSizeOfRepositories()
print("Average Size of Repositories (in kilobytes):")
print(averageSizeOfRepositories)

averageForksOfRepositories = viewRepository.getAverageForksOfRepositories()
print("Average Number of Forks per Repositories:")
print(averageForksOfRepositories)

averageWatchersOfRepositories = viewRepository.getAverageWatchersOfRepositories()
print("Average Number of Watchers per Repositories:")
print(averageWatchersOfRepositories)

averageSubscribersOfRepositories = viewRepository.getAverageSubscribersOfRepositories()
print("Average Number of Subscribers per Repositories:")
print(averageSubscribersOfRepositories)

from view_model import ViewModel
import matplotlib.pyplot as plt
import numpy as np

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
# make the plot
#y_pos = np.arange(len(languages['language']))
#plt.barh(y_pos, languages['Number of Repositories'])
#plt.yticks(y_pos, languages['language'])
#plt.show()

countries = viewRepository.getNumberOfReposPerCountry()
print(countries)
#y_pos = np.arange(len(countries['country']))
#plt.barh(y_pos, countries['Number of Repositories'])
#plt.yticks(y_pos, countries['country'])
#plt.show()

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

stars = viewRepository.getNumberOfReposPerStars()
print(stars)
#plt.hist(stars['stars'], bins=1000, edgecolor='black', linewidth=1.0)
#plt.xlabel("Number of Stars")
#plt.ylabel("Number of Repositories")
#plt.show()

# ============================= Data with the 100 Repositories most popular ==========================================

reposMostPopular = viewRepository.get100ReposMostPopular_StepsPerScenario()
print(reposMostPopular)
plt.boxplot(reposMostPopular['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in 100 Most Popular Repositories")
plt.ylabel("Steps in one Scenario")
plt.show()

reposMostPopular = viewRepository.get100ReposMostPopular_ScenarioPerFeature()
print(reposMostPopular)
plt.boxplot(reposMostPopular['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in 100 Most Popular Repositories")
plt.ylabel("Scenarios in one Feature")
plt.show()

reposMostPopular = viewRepository.get100ReposMostPopular_FeaturePerSize()
print(reposMostPopular)
plt.plot(reposMostPopular["size"], reposMostPopular["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in 100 Most Popular Repositories")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.grid()
plt.show()

languages = viewRepository.get100ReposMostPopular_Languages()
print(languages)
y_pos = np.arange(len(languages['language']))
plt.barh(y_pos, languages['Number of Repositories'])
plt.yticks(y_pos, languages['language'])
plt.title("Number of Repositories per Language in 100 Most Popular Repositories")
plt.ylabel("Language")
plt.xlabel("Number of Repositories")
plt.show()


# ====================================================================================================================

# ============================= Data with the 100 Repositories most forks ============================================

reposMostForks = viewRepository.get100ReposMostForks_StepsPerScenario()
print(reposMostForks)
plt.boxplot(reposMostForks['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in 100 Repositories with most forks")
plt.ylabel("Steps in one Scenario")
plt.show()

reposMostForks = viewRepository.get100ReposMostForks_ScenarioPerFeature()
print(reposMostForks)
plt.boxplot(reposMostForks['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in 100 Repositories with most forks")
plt.ylabel("Scenarios in one Feature")
plt.show()

reposMostForks = viewRepository.get100ReposMostForks_FeaturePerSize()
print(reposMostForks)
plt.plot(reposMostForks["size"], reposMostForks["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in 100 Repositories with most forks")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.show()

languages = viewRepository.get100ReposMostForks_Languages()
print(languages)
y_pos = np.arange(len(languages['language']))
plt.barh(y_pos, languages['Number of Repositories'])
plt.yticks(y_pos, languages['language'])
plt.title("Number of Repositories per Language in 100 Repositories with most forks")
plt.ylabel("Language")
plt.xlabel("Number of Repositories")
plt.show()

# ====================================================================================================================

# ============================= Data with the 100 Repositories most recent ===========================================

reposMostRecent = viewRepository.get100ReposMostRecent_StepsPerScenario()
print(reposMostRecent)
plt.boxplot(reposMostRecent['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in 100 most recent Repositories")
plt.ylabel("Steps in one Scenario")
plt.show()

reposMostRecent = viewRepository.get100ReposMostRecent_ScenarioPerFeature()
print(reposMostRecent)
plt.boxplot(reposMostRecent['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in 100 most recent Repositories")
plt.ylabel("Scenarios in one Feature")
plt.show()

reposMostRecent = viewRepository.get100ReposMostRecent_FeaturePerSize()
print(reposMostRecent)
plt.plot(reposMostRecent["size"], reposMostRecent["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in 100 Most Recent Repositories")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.show()

languages = viewRepository.get100ReposMostRecent_Languages()
print(languages)
y_pos = np.arange(len(languages['language']))
plt.barh(y_pos, languages['Number of Repositories'])
plt.yticks(y_pos, languages['language'])
plt.title("Number of Repositories per Language in 100 most recent Repositories")
plt.ylabel("Language")
plt.xlabel("Number of Repositories")
plt.show()

# ====================================================================================================================

# ===================================== Data with the Java Repositories ==============================================

repos = viewRepository.getJavaRepos_StepsPerScenario()
print(repos)
plt.boxplot(repos['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in Java Repositories")
plt.ylabel("Steps in one Scenario")
plt.show()

repos = viewRepository.getJavaRepos_ScenarioPerFeature()
print(repos)
plt.boxplot(repos['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in Java Repositories")
plt.ylabel("Scenarios in one Feature")
plt.show()

repos = viewRepository.getJavaRepos_FeaturePerSize()
print(repos)
plt.plot(repos["size"], repos["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in Java Repositories")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.show()


# ====================================================================================================================

# ===================================== Data with the JavaScript Repositories ========================================

repos = viewRepository.getJavaScriptRepos_StepsPerScenario()
print(repos)
plt.boxplot(repos['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in JavaScript Repositories")
plt.ylabel("Steps in one Scenario")
plt.show()

repos = viewRepository.getJavaScriptRepos_ScenarioPerFeature()
print(repos)
plt.boxplot(repos['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in JavaScript Repositories")
plt.ylabel("Scenarios in one Feature")
plt.show()

repos = viewRepository.getJavaScriptRepos_FeaturePerSize()
print(repos)
plt.plot(repos["size"], repos["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in JavaScript Repositories")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.show()


# ====================================================================================================================

# ===================================== Data with the Python Repositories ============================================

repos = viewRepository.getPythonRepos_StepsPerScenario()
print(repos)
plt.boxplot(repos['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in Python Repositories")
plt.ylabel("Steps in one Scenario")
plt.show()

repos = viewRepository.getPythonRepos_ScenarioPerFeature()
print(repos)
plt.boxplot(repos['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in Python Repositories")
plt.ylabel("Scenarios in one Feature")
plt.show()

repos = viewRepository.getPythonRepos_FeaturePerSize()
print(repos)
plt.plot(repos["size"], repos["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in Python Repositories")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.show()


# ====================================================================================================================

# ===================================== Data with the Ruby Repositories ==============================================

repos = viewRepository.getRubyRepos_StepsPerScenario()
print(repos)
plt.boxplot(repos['Number of Steps'])
plt.yscale("log")
plt.title("Number of Steps per Scenario in Ruby Repositories")
plt.ylabel("Steps in one Scenario")
plt.show()

repos = viewRepository.getRubyRepos_ScenarioPerFeature()
print(repos)
plt.boxplot(repos['Number of Scenarios'])
plt.yscale("log")
plt.title("Number of Scenarios per Feature in Ruby Repositories")
plt.ylabel("Scenarios in one Feature")
plt.show()

repos = viewRepository.getRubyRepos_FeaturePerSize()
print(repos)
plt.plot(repos["size"], repos["Number of Features"], linestyle='-', marker='o', color='blue')
plt.title("Number of Features per Repository in Ruby Repositories")
plt.xlabel("Size of Repository")
plt.ylabel("Number of Features")
plt.xscale("log")
plt.show()


# ====================================================================================================================
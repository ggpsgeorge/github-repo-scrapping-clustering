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

numberOfRepositories = viewRepository.getNumberOfTotalRepositories()
print("Number of repositories: ")
print(numberOfRepositories)

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

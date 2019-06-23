from view_model import ViewModel
import matplotlib.pyplot as plt

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

viewRepository.getReposAsObject()

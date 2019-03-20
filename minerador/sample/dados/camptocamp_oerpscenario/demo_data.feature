###############################################################################
#
#    OERPScenario, OpenERP Functional Tests
#    Copyright 2009 Camptocamp SA
#
##############################################################################

# Features Generic tags (none for all)
##############################################################################

# System
@demo 

Feature: check base
  In order to load the demo data for installed module
      
  Scenario: Install demo datas on installed modules
    Given I want to load the demo data on all installed modules
    When I tic the demo data field on all found modules
    And ask to upgrade the base module
    And run the update
    Then I should see some demo data loaded
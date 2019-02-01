@Complete
Feature: App Access
  As a giffgaff member I want to have access to the giffgaff APP.

  @login
  Scenario: Log in to the giffgaff App
    Given I am not logged in
    When I log in as 'eyalyovel'
    Then I am logged in as 'eyalyovel'


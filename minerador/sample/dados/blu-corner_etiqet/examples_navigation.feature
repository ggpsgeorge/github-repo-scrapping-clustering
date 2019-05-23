Feature: Navigating

  Background:
    Given I open the browser

  Scenario: Opening url
    Given I go to the url "https://www.ultimateqa.com"

  Scenario: Using back and forward
    Given I go to the url "https://www.ultimateqa.com"
      And I go to the url "https://www.ultimateqa.com/complicated-page/"
    Then I go forward a page
    Then I go back a page

  Scenario: Refreshing the page
    Given I go to the url "https://www.ultimateqa.com"
      And I refresh the page

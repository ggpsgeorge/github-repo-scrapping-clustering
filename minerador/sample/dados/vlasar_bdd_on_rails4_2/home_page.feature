Feature: Home page

  # Even though the feature isn't using any JS we want to make sure the browser opens
  @javascript
  Scenario: Viewing application's homepage
    Given there's a post titled "First scenario" with "Hello, BDD World!" content 
    When I am on the homepage
    Then I should see the "First scenario" post

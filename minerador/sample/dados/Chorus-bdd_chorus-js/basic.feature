Uses: Web Sockets
Uses: Selenium
Uses: Chorus Context

Feature: Basic steps

  Feature-Start:
    Given I start a web socket server
    And I open the RemoteWebDriver browser
    And I navigate to ${exampleAppURL}
    And I wait for the web socket client SimpleStepPublisher

  Scenario: I can call steps with and without a result
    Check I can call a step with a result
    And I can call a step without a result

  Scenario: I can call steps which fail
    Check I can call a step with a result
    And I can call a step which fails

  Scenario: I can call steps which are async
    Check I can call a step which succeeds asynchronously
    And I can call a step which times out

  Scenario: I can read a variable from the Chorus Context
    Given I create a context variable outbound with the value one
    Then in chorus-js 'outbound' has the value 'one'

  Scenario: I can set a variable in the Chorus Context
    When I set the 'inbound' variable to 'two' in chorus-js
    Then the context variable inbound has the value two

  Scenario: I can overwrite a variable in the Chorus Context
    Given I create a context variable outbound with the value two
    When I set the 'outbound' variable to 'three' in chorus-js
    Then the context variable outbound has the value three

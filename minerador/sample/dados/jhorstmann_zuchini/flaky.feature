Feature: Automatically rerun failing tests

  Scenario: A scenario that succeeds on the second try
    Given a step that succeeds on the second try

  Scenario: A scenario that succeeds on the third try
    Given a successful step
    And a step that succeeds on the third try

  Scenario: A successful scenario
    Given a successful step

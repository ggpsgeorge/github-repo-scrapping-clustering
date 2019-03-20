Feature: jx create spring
  As a developer
  I need to be able to create and delete a new spring boot application with CI / CD

  Scenario: Create and delete a new Spring Boot application
    Given a work directory
    When running "jx create spring -d web -d actuator -l java --group com.acme" in that directory
    Then there should be a jenkins project created
    And the application should be built and promoted via CI / CD
    And the application should be deleted after running jx delete app
    And the git repo should be deleted after running jx delete repo

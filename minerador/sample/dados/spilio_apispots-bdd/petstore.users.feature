Feature: Swagger Petstore - Pets
  As a client of the Petstore API
  I want to run tests
  In order to validate User related operations

  Background:
    Given a "Swagger" API definition at "http://petstore.swagger.io/v2/swagger.json"

  Scenario: Create a new user
    Given an operation with Id "createUser"
    And request body
      """
      {
      "id": "12345",
      "username": "thechef",
      "firstName": "chris",
      "lastName": "spilio",
      "password": "thepass"
      }
      """
    And request type "application/json"
    When the request is executed
    Then response status is "ok"

  Scenario: Getting the user by username
    Given the endpoint "/user/{username}" and method "get"
    And request path param "username" equals "thechef"
    When the request is executed
    Then response status is "ok"

  Scenario: Getting the user by username - bad username
    Given an operation with Id "getUserByName"
    And request path param "username" equals "koukouroukou123213121dsqsaddads"
    When the request is executed
    Then response status is "notFound"

  Scenario: Getting the user by username - timed out
    Given the endpoint "/user/{username}" and method "get"
    And request path param "username" equals "thechef"
    And request timeout is "100"
    When the request is executed
    Then response has time out error

  Scenario: Update the user
    Given an operation with Id "updateUser"
    And request path param "username" equals "thechef"
    And request body
      """
      {
      "username": "thechef",
      "firstName": "chrysanthos",
      "lastName": "spiliotopoulos",
      "phone": "123456"
      }
      """
    And request type "application/json"
    When the request is executed
    Then response status is "ok"

  Scenario: Getting the updated user details
    Given an operation with Id "getUserByName"
    And request path param "username" equals "thechef"
    When the request is executed
    Then response status is "ok"
    And response body has attributes
      | attribute | value |
      | firstName | 'chrysanthos' |
      | lastName | 'spiliotopoulos' |
      | phone | "123456" |

  Scenario: Login the user
    Given an operation with Id "loginUser"
    And request query params
      | param | value |
      | username | 'thechef' |
      | password | 'thepass' |
    When the request is executed
    Then response status is "ok"

  Scenario: Logout the user
    Given an operation with Id "logoutUser"
    When the request is executed
    Then response status is "ok"

  Scenario: Delete the user
    Given an operation with Id "deleteUser"
    And request path param "username" equals "thechef"
    When the request is executed
    Then response status is "ok"

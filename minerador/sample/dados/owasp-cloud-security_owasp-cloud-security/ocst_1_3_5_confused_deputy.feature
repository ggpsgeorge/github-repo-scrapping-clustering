# Id: OCST-1.3.5
# Status: Confirmed
# Service: AWS IAM
# STRIDE:
#   - Elevation of privilege
# Components:
#   - IAM AssumeRole
# References:
#   - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html
#   - https://aws.amazon.com/blogs/security/tag/confused-deputy/


Feature: Confused deputy attack
  In order to gain access to resources in another account
  As an attacker
  I want a third party to be vulnerable to a confused deputy attack


  Background:
    Given a third party with access to resources in the attackers account via an ARN
    And the third party has access to resources in the target account via an ARN
    And the attacker can guess the target accounts ARN


  Scenario: Confused deputy attack with no ExternalId
    Given the ExternalId attribute is not used by the third party
    When the attacker swaps its own ARN for the target ARN
    And the third party performs its actions on resources using the target ARN
    Then the attacker successfully agains access to the target resources


  Scenario: Confused deputy attack with a weak ExternalId
    Given the ExternalId attribute is required by the third party
    But the ExternalId attribute has no complexity enforced
    When the attacker swaps its own ARN for the target ARN
    And the attacker guesses the ExternalId
    And the third party performs its actions on resources using the target ARN
    Then the attacker successfully agains access to the target resources
    And the attacker successfully guessed the correct ExternalId

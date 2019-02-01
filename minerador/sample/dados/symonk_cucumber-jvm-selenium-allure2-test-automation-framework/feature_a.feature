@feature-one @regression
Feature: Feature number 1
  As a brilliant and caring individual
  I want to be able to adopt a puppy
  So that I can do a lil' good in the world

  @issue=001 @tmsLink=002 @severity.Critical
  Scenario: User adopts a puppy 002
    Given an order has been prepared
    When the order is processed
    Then the adoption successful message is shown

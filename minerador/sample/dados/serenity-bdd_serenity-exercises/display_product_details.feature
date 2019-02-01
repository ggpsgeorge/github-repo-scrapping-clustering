Feature: Display product details
  In order to encourage buyers to make a purchase
  As a seller
  I want buyers to be able to see details about a product

  Scenario: Display product details from the search list
    Given I have searched for 'Spoon'
    When I select item 1
    Then I should see product description and price on the details page
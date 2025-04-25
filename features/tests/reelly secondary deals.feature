Feature: Reelly

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open reelly main page
    When Enter email
    And Enter password
    And Click continue button
    And Click on the “Secondary” option at the left side menu
    Then Verify the right page opens
    And Click Filter button
    Then Wait for side Navigation to pop up
    And Filter products by want to sell
    When Click Apply Filter button
    Then Verify every product has for sale tag







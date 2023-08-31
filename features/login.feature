Feature: Check the functionality of the login page
  # Scenario 1: correct username + correct password
  # Scenariu 2: username gresit + parola corecta
  # Scenariu 3: username corect + parola gresita
  # Scenariu 4: username corect + parola None
  # Scenariu 5: username None + parola corecta
  # Scenariu 6: username incorect + parola None
  # Scenariu 7: username None + parola incorecta
  # Scenariu 8: username None + parola None
  # Scenariu 9: username gresit + parola gresita

  Scenario: Login in application with correct username and correct password
    Given I am on the login page
    When I introduce correct username and correct password
    And I click on the login button
    Then I can login in the application and I can see the product list

  Scenario: Login in application with incorrect username and correct password
    Given I am on the login page
    When I introduce incorrect username and correct password
    And I click on the login button
    Then I can not login in the application and I see an error
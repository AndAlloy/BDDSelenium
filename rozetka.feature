# behave .\features\rozetka.feature --------- RUN
Feature:
  Scenario: Search item
    Given launch chrome browser with website
    When input search text
    And run search

  Scenario: Sort by price
    Given launch chrome browser with laptops category
    When open sort dropdown
    When select sort option = "Новинки"
    Then check sort option = "Новинки"

  Scenario: Switch language
    Given launch chrome browser with website
    When switch website language
    Then assert current language

#  Scenario: Add item to cart
#    Given launch chrome browser with suburl = "ua/samsung-sm-a245fzkvsek/p375225780/"
#    When find and click characteristics button on item page
#    Then click comments button on item page

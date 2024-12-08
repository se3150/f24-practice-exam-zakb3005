Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    When I set the element with id "a" to "6"
    When I set the element with id "b" to "6"
    When I set the element with id "c" to "6"
    When I click the element with id "clcbtn"
    Then the element with id "_d" should contain text "15.588"

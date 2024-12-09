Feature: calculate the area of a triangle
  As an aspiring mathematician
  I should be able to calculate the area of a triangle
  So that I can chat with my math friends like a pro

Scenario: I can calculate the area of a triangle
  Given I open the url "https://byjus.com/herons-calculator/"
  When I set "6" to the inputfield "#a"
  When I set "6" to the inputfield "#b"
  When I set "6" to the inputfield "#c"
  When I click on the element ".clcbtn"
  Then I expect that element "#_d" contains the text "15.588"
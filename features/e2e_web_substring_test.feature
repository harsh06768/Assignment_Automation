Feature: Validate Agrichain Substring Length Output

  Scenario Outline: Enter a string and verify longest unique substring length
    Given I launch the browser and open the input page
    When I enter the string "<input_text>" and click submit
    Then I switch to the result tab
    And I should see output "<expected_output>"
-
    Examples:
      | input_text | expected_output |
      | abcabcbb   | 3               |
      | abc@1234   | 7               |
      |            | 0               |
      | aaaaa      | 1               | 
      | !@#$#@     | 4               |  

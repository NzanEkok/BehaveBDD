Feature: Add New User

  Scenario: Create new user
     Given launch chrome browser
      When open test application
      And enter First Name "Patrick"
      And enter Middle Name "Ekok"
      And enter Last Name "Nzan"
      And enter Phone Number "8093893394"
      And Select Date of birth "11/15/2022"
      And enter Address "Road 5 Epe, Lagos"
      And click on "Add New User" button
      Then Add new user!
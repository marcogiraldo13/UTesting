Feature: gestionar libros

  Background:
    Given Estoy en la url del API

  Scenario: consultar todos los libros
    When Consulto todos los libros
    Then Trae todos los libros

    Scenario: consultar un libro
      When consulto un libro con codigo "id"
      Then trae la informacion de ese libro
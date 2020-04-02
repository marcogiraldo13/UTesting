Feature: gestionar autores

  Background:
    Given Estoy en la url del API

  Scenario: consultar todos los autores
    When Consulto todos los autores
    Then Trae todos los autores

    Scenario: consultar un autor
      When consulto un autor con codigo "id"
      Then trae la informacion de ese autor
Feature: gestionar libros

  Background:
    Given Estoy en la url del API

  Scenario: consultar todas las portadas
    When Consulto todas las portadas
    Then Trae todas las portadas

    Scenario: consultar una portada
      When consulto una portada con codigo "id"
      Then trae la informacion de esa portada
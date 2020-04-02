Feature: gestionar libros

  Background:
    Given Estoy en la url del API

  Scenario: consultar todos los usuarios
    When Consulto todos los usuarios
    Then Trae todos los usuarios

    Scenario: consultar un usuario
      When consulto un usuario con codigo "id"
      Then trae la informacion de ese usuario
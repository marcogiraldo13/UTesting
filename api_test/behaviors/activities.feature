Feature: gestionar actividades

  Background:
    Given Estoy en la url del API

  Scenario: consultar todas las actividades
    When Consulto todas las actividades
    Then Trae todas las actividades

    Scenario: consultar una actividad
      When consulto una actividad con codigo "id"
      Then trae la informacion de esa actividad
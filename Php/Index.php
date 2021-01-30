<?php
require_once("Car.php");
require_once("Account.php");

$car = new Car("SDL123", new Account("Paco", "111111111"));
$car->printDataCar();
?>
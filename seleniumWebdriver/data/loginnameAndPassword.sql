SELECT DISTINCT edu_auth.`account`.loginName, edu_auth.`account`.`password` 
FROM edu_auth.`account` JOIN  account 
ON account.sourceSystem = "10001" AND edu_auth.`account`.`status` = "2" AND edu_auth.`account`.`password`="14e1b600b1fd579f47433b88e8d85291"
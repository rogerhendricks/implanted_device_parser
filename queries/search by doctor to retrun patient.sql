SELECT cardiologist_id AS [ cardiologist ID ], p.name_given AS [ p Firstname], p.name_family AS [p Lastname], doc.first_name AS [doc first_name], doc.last_name AS [ doc last_name]  
FROM patient p
INNER JOIN cardiologist doc on doc.id = p.cardiologist_id
WHERE p.serial = '123456';
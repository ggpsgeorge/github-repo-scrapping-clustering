# language: ru

@IgnoreOn82Builds
@IgnoreOnOFBuilds
@IgnoreOnWeb

Функционал: Остановка и продолжение выполнения сценария перед началом сценария
	Как Разработчик
	Я Хочу чтобы у меня была возможность поместить файл в процедуре перед началом сценария и использовать ЗапретитьВыполнениеШагов
	Чтобы это не вызывало ошибок в отдельном сеансе

Сценарий: Остановка и продолжение выполнения сценария перед началом сценария
	Когда я открыл форму VanessaBehavoir в режиме самотестирования
	И я загрузил специальную тестовую фичу "ПомещениеФайлаПередНачаломСценарияTemplate"
	И Пауза 1
	И я прервал выполнение шагов в хост системе и я нажал на кнопку "ВыполнитьСценарии"

# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload) - O python não suporta
# Sobreposição de métodos (override) - O Python suporta

from abc import abstractmethod, ABC


class Notification(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def send(self) -> bool:
        pass


class NotificationEmail(Notification):
    def send(self) -> bool:
        print('Enviando E-mail: - ', self.msg)
        return True


class NotificationSms(Notification):
    def send(self) -> bool:
        print('Enviando SMS: - ', self.msg)
        return True


def notify(notification: Notification):
    notifcation_sent = notification.send()

    if notifcation_sent:
        print('Notificação enviada.')
    else:
        print('Notificação não foi enviada.')


email_notification = NotificationEmail('Testando msg via e-mail')
sms_notification = NotificationSms('Testando msg via sms')

notify(email_notification)
notify(sms_notification)

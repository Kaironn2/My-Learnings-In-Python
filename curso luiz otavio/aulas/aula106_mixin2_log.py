# Abstração

LOG_FILE = 'C:\\Users\\jonat\\OneDrive\\Área de Trabalho\\Py\\Python\\Outros Arquivos\\log_file.txt'

counter = 1


class Log:
    def _log(self, msg):  # a linha de definição do metodo se chama "assinatura do método"
        raise NotImplementedError(
            'Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):  # Não devemos mudar a assinatura do método, para não quebrar um príncipio
        global counter
        msg_formated = (f'{msg} ({self.__class__.__name__})')
        print(f'{counter} - Salvando no log:')
        counter += 1
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formated)
            file.write('\r\n')


class LogPrintMixin(Log):
    def _log(self, msg):  # Não devemos mudar a assinatura do método, para não quebrar um príncipio
        print(msg, self.__class__.__name__)


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_sucess('Logado!')
    lp.log_error('Não logou!')
    lf = LogFileMixin()
    lf.log_error('Não logou')
    lf.log_sucess('logado!')

from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_SUFFIX}'
        self.MirrorCommand = [f'mirror2{CMD_SUFFIX}', f'm2{CMD_SUFFIX}']
        self.UnzipMirrorCommand = [
            f'unzipmirror2{CMD_SUFFIX}', f'uzm2{CMD_SUFFIX}']
        self.ZipMirrorCommand = [f'zipmirror2{CMD_SUFFIX}', f'zm3{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror2{CMD_SUFFIX}', f'qm2{CMD_SUFFIX}']
        self.QbUnzipMirrorCommand = [
            f'qbunzipmirror2{CMD_SUFFIX}', f'quzm2{CMD_SUFFIX}']
        self.QbZipMirrorCommand = [
            f'qbzipmirror2{CMD_SUFFIX}', f'qzm2{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl2{CMD_SUFFIX}', f'y2{CMD_SUFFIX}']
        self.YtdlZipCommand = [f'ytdlzip2{CMD_SUFFIX}', f'yz2{CMD_SUFFIX}']
        self.LeechCommand = [f'leech2{CMD_SUFFIX}', f'l2{CMD_SUFFIX}']
        self.UnzipLeechCommand = [
            f'unzipleech2{CMD_SUFFIX}', f'uzl2{CMD_SUFFIX}']
        self.ZipLeechCommand = [f'zipleech2{CMD_SUFFIX}', f'zl2{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech2{CMD_SUFFIX}', f'ql2{CMD_SUFFIX}']
        self.QbUnzipLeechCommand = [
            f'qbunzipleech2{CMD_SUFFIX}', f'quzl2{CMD_SUFFIX}']
        self.QbZipLeechCommand = [
            f'qbzipleech2{CMD_SUFFIX}', f'qzl2{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech2{CMD_SUFFIX}', f'yl2{CMD_SUFFIX}']
        self.YtdlZipLeechCommand = [
            f'ytdlzipleech2{CMD_SUFFIX}', f'yzl2{CMD_SUFFIX}']
        self.CloneCommand = f'clone2{CMD_SUFFIX}'
        self.CountCommand = f'count2{CMD_SUFFIX}'
        self.DeleteCommand = f'delete2{CMD_SUFFIX}'
        self.CancelMirror = f'cancel2{CMD_SUFFIX}'
        self.CancelAllCommand = f'cancelall2{CMD_SUFFIX}'
        self.ListCommand = f'list2{CMD_SUFFIX}'
        self.SearchCommand = f'search2{CMD_SUFFIX}'
        self.StatusCommand = [f'status2{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'sall']
        self.UsersCommand = f'users2{CMD_SUFFIX}'
        self.AuthorizeCommand = f'auth2{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauth2{CMD_SUFFIX}'
        self.AddSudoCommand = f'addsudo2{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo2{CMD_SUFFIX}'
        self.PingCommand = f'ping{CMD_SUFFIX}'
        self.RestartCommand = f'restart2{CMD_SUFFIX}'
        self.StatsCommand = f'stats2{CMD_SUFFIX}'
        self.HelpCommand = f'help2{CMD_SUFFIX}'
        self.LogCommand = f'log2{CMD_SUFFIX}'
        self.ShellCommand = f'shell2{CMD_SUFFIX}'
        self.EvalCommand = f'eval2{CMD_SUFFIX}'
        self.ExecCommand = f'exec2{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals2{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting2{CMD_SUFFIX}'
        self.UserSetCommand = f'usetting2{CMD_SUFFIX}'
        self.BtSelectCommand = f'btsel2{CMD_SUFFIX}'
        self.RssCommand = f'rss2{CMD_SUFFIX}'


BotCommands = _BotCommands()

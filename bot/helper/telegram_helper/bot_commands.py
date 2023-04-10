from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_SUFFIX}'
        self.MirrorCommand = [f'mirror1{CMD_SUFFIX}', f'm1{CMD_SUFFIX}']
        self.UnzipMirrorCommand = [
            f'unzipmirror1{CMD_SUFFIX}', f'uzm1{CMD_SUFFIX}']
        self.ZipMirrorCommand = [f'zipmirror1{CMD_SUFFIX}', f'zm1{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror1{CMD_SUFFIX}', f'qm1{CMD_SUFFIX}']
        self.QbUnzipMirrorCommand = [
            f'qbunzipmirror1{CMD_SUFFIX}', f'quzm1{CMD_SUFFIX}']
        self.QbZipMirrorCommand = [
            f'qbzipmirror1{CMD_SUFFIX}', f'qzm1{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl1{CMD_SUFFIX}', f'y1{CMD_SUFFIX}']
        self.YtdlZipCommand = [f'ytdlzip1{CMD_SUFFIX}', f'yz1{CMD_SUFFIX}']
        self.LeechCommand = [f'leech1{CMD_SUFFIX}', f'l1{CMD_SUFFIX}']
        self.UnzipLeechCommand = [
            f'unzipleech1{CMD_SUFFIX}', f'uzl1{CMD_SUFFIX}']
        self.ZipLeechCommand = [f'zipleech1{CMD_SUFFIX}', f'zl1{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech1{CMD_SUFFIX}', f'ql1{CMD_SUFFIX}']
        self.QbUnzipLeechCommand = [
            f'qbunzipleech1{CMD_SUFFIX}', f'quzl1{CMD_SUFFIX}']
        self.QbZipLeechCommand = [
            f'qbzipleech1{CMD_SUFFIX}', f'qzl1{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech1{CMD_SUFFIX}', f'yl1{CMD_SUFFIX}']
        self.YtdlZipLeechCommand = [
            f'ytdlzipleech1{CMD_SUFFIX}', f'yzl1{CMD_SUFFIX}']
        self.CloneCommand = f'clone1{CMD_SUFFIX}'
        self.CountCommand = f'count1{CMD_SUFFIX}'
        self.DeleteCommand = f'delete1{CMD_SUFFIX}'
        self.CancelMirror = f'cancel1{CMD_SUFFIX}'
        self.CancelAllCommand = f'cancelall1{CMD_SUFFIX}'
        self.ListCommand = f'list1{CMD_SUFFIX}'
        self.SearchCommand = f'search1{CMD_SUFFIX}'
        self.StatusCommand = [f'status1{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'sall']
        self.UsersCommand = f'users1{CMD_SUFFIX}'
        self.AuthorizeCommand = f'auth1{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauth1{CMD_SUFFIX}'
        self.AddSudoCommand = f'addsudo1{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo1{CMD_SUFFIX}'
        self.PingCommand = f'ping{CMD_SUFFIX}'
        self.RestartCommand = f'restart1{CMD_SUFFIX}'
        self.StatsCommand = f'stats1{CMD_SUFFIX}'
        self.HelpCommand = f'help1{CMD_SUFFIX}'
        self.LogCommand = f'log1{CMD_SUFFIX}'
        self.ShellCommand = f'shell1{CMD_SUFFIX}'
        self.EvalCommand = f'eval1{CMD_SUFFIX}'
        self.ExecCommand = f'exec1{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals1{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting1{CMD_SUFFIX}'
        self.UserSetCommand = f'usetting1{CMD_SUFFIX}'
        self.BtSelectCommand = f'btsel1{CMD_SUFFIX}'
        self.RssCommand = f'rss1{CMD_SUFFIX}'


BotCommands = _BotCommands()

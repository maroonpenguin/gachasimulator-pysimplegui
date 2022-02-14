from random import random
import PySimpleGUI as sg

sg.theme('LightGreen')

menu_def = [['ファイル', ['ロード', 'セーブ', '---', '終了']],
            ['ヘルプ', 'About...']]
# target
frame11 = sg.Frame('ターゲット',
                   [
                       [
                           sg.Text('レアリティ:', font="meiryo"),
                           sg.Combo(['SSR', '★★★'], '★★★', readonly=True,
                                    key='-RARE-', size=(5, 1), font="meiryo"),
                           sg.Button('切替', key='-R_STAR-', size=(5, 1),
                                     font="meiryo"),
                           sg.Text('確率(%) :', font="meiryo"),
                           sg.Input('0.750', disabled=False,
                                    key='-TAR_PER-', size=(5, 1),
                                    font="meiryo"),
                       ],
                       [
                           sg.Text('名前 :', font="meiryo"),
                           sg.Input('メジロアルダン', disabled=False,
                                    key='-NAME-', font="meiryo"),
                       ],
                       [
                           sg.Button('セーブ', key="-SAVE-", size=(5, 1),
                                     font="meiryo", pad=((260, 0), (0, 0))),
                           sg.Button('ロード', key="-LOAD-", size=(5, 1),
                                     font="meiryo", pad=((10, 0), (0, 0))),
                       ],
                       [
                           # blank
                           sg.Text('')
                       ],
                       [
                           # SSR and ★★★
                           sg.Input('★★★', disabled=False,
                                    key='-SSR-', size=(5, 1),
                                    font="meiryo"),
                           sg.Text('確率(%) :', font="meiryo"),
                           sg.Input('3', disabled=False,
                                    key='-SSR_PER-', size=(5, 1),
                                        font="meiryo"),
                           sg.Text('種類 :', font="meiryo"),
                           sg.Input('50', disabled=False,
                                    key='-SSR_TYPES-', size=(11, 1),
                                        font="meiryo"),
                       ],
                       [
                           # SR and ★★
                           sg.Input('★★', disabled=False,
                                    key='-SR-', size=(5, 1),
                                        font="meiryo"),
                           sg.Text('確率(%) :',  font="meiryo"),
                           sg.Input('18', disabled=False,
                                    key='-SR_PER-', size=(5, 1),
                                    font="meiryo"),
                           sg.Text('種類 :', font="meiryo"),
                           sg.Input('8', disabled=False,
                                    key='-SR_TYPES-', size=(11, 1),
                                    font="meiryo"),
                       ],
                       [
                           # R and ★
                           sg.Input('★', disabled=False,
                                    key='-R-', size=(5, 1),
                                        font="meiryo"),
                           sg.Text('確率(%) :',  font="meiryo"),
                           sg.Input('79', disabled=False,
                                    key='-R_PER-', size=(5, 1),
                                        font="meiryo"),
                           sg.Text('種類 :', font="meiryo"),
                           sg.Input('8', disabled=False,
                                    key='-R_TYPES-', size=(11, 1),
                                        font="meiryo"),
                       ],
                       [
                           # blank
                           sg.Text('')
                       ],
                       [
                           # button
                           sg.Button('1連', key='-ONE-',
                                     size=(5, 1), font="meiryo"),
                           sg.Button('10連', key='-TEN-',
                                     size=(5, 1), font="meiryo"),
                           sg.Text('',
                                   key='-ERROR-', font="meiryo",
                                   text_color="red")
                       ],
                       [
                           sg.Button('初期化', key='-DEFAULT-',
                                     size=(5, 1), font="meiryo")
                       ]
                   ], size=(400, 700), font="meiryo"
                   )

frame21 = sg.Frame('結果',

                   [
                       [
                           sg.Button('ログクリア', key="-LOG_CLEAR-",
                                     size=(10, 1), font="meiryo"),
                           sg.Text('合計', font="meiryo"),
                           sg.Input('0連', disabled=True,
                                    key='-COUNT-', size=(5, 1),
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_0-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_1-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_2-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_3-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_4-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_5-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_6-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_7-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_8-',
                                    font="meiryo")
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-RES_9-',
                                    font="meiryo")
                       ],
                       [
                           sg.Text('')
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-GET_TARGET-',
                                    font="meiryo")
                       ]
                   ], size=(400, 700), font="meiryo"
                   )


layout = [
    [
        [sg.Menu(menu_def,)],
        frame11,
        frame21
    ]
]

window = sg.Window('GachaSimulator -ver 0.3.0-', layout, resizable=True)

count = 0


def gacha_result(res):
    def value_result(ssr: str, value: str) -> None:
        window[ssr].update(value)

    for i in range(len(res)):
        if res[i] == values['-SSR-']:
            value_result('-RES_' + str(i) + '-', values['-SSR-'])
        elif res[i] == values['-SR-']:
            value_result('-RES_' + str(i) + '-', values['-SR-'])
        elif res[i] == values['-R-']:
            value_result('-RES_' + str(i) + '-', values['-R-'])
        else:
            value_result('-RES_' + str(i) + '-', values['-RARE-'] +
                         ':' + values['-NAME-'] + 'を入手')


def gacha_detail(val):
    res = []
    for i in range(val):
        random_int = int(random()*100000)
        target_int = int(float(values['-TAR_PER-']) * 1000)
        ssr_int = int(float(values['-SSR_PER-']) * 1000)
        sr_int = int(float(values['-SR_PER-']) * 1000)
        if ssr_int < target_int:
            window['-ERROR-'].update('エラー')
            break
        elif 0 < random_int <= target_int:
            res.append('【' + values['-SSR-'] + '】')
        else:
            if target_int < random_int <= ssr_int:
                res.append(values['-SSR-'])
            elif ssr_int < random_int <= (ssr_int + sr_int):
                res.append(values['-SR-'])
            else:
                if i == 9:
                    res.append(values['-SR-'])
                else:
                    res.append(values['-R-'])
        if '【' + values['-SSR-'] + '】' in res:
            window['-GET_TARGET-'].update(str(count) +
                                          '連で' + values['-NAME-'] + 'を入手')
        if count == 200:
            window['-GET_TARGET-'].update(str(count) +
                                          '連で' + values['-NAME-'] + 'を確定入手')
    gacha_result(res)


while True:
    event, values = window.read()

    # menu
    if event is None or event == '終了':
        print('exit')
        break

    if event == 'About...':
        sg.popup('このアプリについて', 'GachaSimulator', 'ver 0.3.0',  font="meiryo")

    if event == '-SAVE-' or event == 'セーブ':
        print("save")

    if event == '-LOAD-' or event == 'ロード':
        print("load")

    # frame1 button
    if event == '-R_STAR-':
        if values['-RARE-'] == 'SSR':
            window['-SSR-'].update('SSR')
            window['-SR-'].update('SR')
            window['-R-'].update('R')
        elif values['-RARE-'] == '★★★':
            window['-SSR-'].update('★★★')
            window['-SR-'].update('★★')
            window['-R-'].update('★')
        else:
            print('Error')

    if event == '-ONE-':
        if (float(values['-SSR_PER-']) + float(values['-SR_PER-']) +
                float(values['-R_PER-'])) > 100:
            window['-ERROR-'].update('エラー:合計100%以下にしてください')
        else:
            count = count + 1
            gacha_detail(1)
            window['-COUNT-'].update(str(count) + '連')
    if event == '-TEN-':
        if (float(values['-SSR_PER-']) + float(values['-SR_PER-']) +
                float(values['-R_PER-'])) > 100:
            window['-ERROR-'].update('エラー:合計100%以下にしてください')
        else:
            count = count + 10
            gacha_detail(10)
            window['-COUNT-'].update(str(count) + '連')
    # default settings
    if event == '-DEFAULT-':
        window['-RARE-'].update('★★★')
        window['-SSR-'].update('★★★')
        window['-SR-'].update('★★')
        window['-R-'].update('★')
        window['-TAR_PER-'].update('0.750')
        window['-NAME-'].update('メジロアルダン')
        window['-SSR_PER-'].update('3')
        window['-SR_PER-'].update('18')
        window['-R_PER-'].update('79')
        window['-ERROR-'].update('')

    # frame2 button
    if event == '-LOG_CLEAR-':
        window['-ERROR-'].update('')
        window['-GET_TARGET-'].update('')
        window['-RES_0-'].update('')
        window['-RES_1-'].update('')
        window['-RES_2-'].update('')
        window['-RES_3-'].update('')
        window['-RES_4-'].update('')
        window['-RES_5-'].update('')
        window['-RES_6-'].update('')
        window['-RES_7-'].update('')
        window['-RES_8-'].update('')
        window['-RES_9-'].update('')
        window['-COUNT-'].update('0')
        count = 0


window.close()

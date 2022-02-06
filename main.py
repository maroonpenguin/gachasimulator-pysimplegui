from random import random
import PySimpleGUI as sg

# sg.theme('TealMono')
# target
frame11 = sg.Frame('ターゲット',
                   [
                       [
                           sg.Text('レアリティ:', font="meiryo"),
                           sg.Combo(['SSR', '★★★'], '★★★', readonly=True,
                                    key='-RARE-', size=(5, 1), font="meiryo"),
                           sg.Button('変更', key='-R_STAR-', size=(5, 1),
                                     font="meiryo"),
                           sg.Text('確率(%) :', font="meiryo"),
                           sg.Input('0.750', disabled=False,
                                    key='-TAR_PER-', size=(5, 1),
                                    font="meiryo"),
                       ],
                       [
                           sg.Text('名前 :', font="meiryo"),
                           sg.Input('ミホノブルボン(バレンタイン)', disabled=False,
                                    key='-NAME-', font="meiryo"),
                       ],
                       [
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
                           sg.Input('', disabled=False,
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
                           #    sg.Button('クリア', key="-CLEAR-",
                           #              size=(7, 1), font="meiryo"),
                           sg.Button('ログクリア', key="-ALL_CLEAR-",
                                     size=(10, 1), font="meiryo"),
                           sg.Text('合計回数 :', font="meiryo"),
                           sg.Input('0', disabled=True,
                                    key='-COUNT-', size=(5, 1),
                                    font="meiryo")
                       ],
                       [
                           sg.Multiline('', key="-RES_LOG-", font="meiryo"),
                       ],
                       [
                           sg.Input('', disabled=True,
                                    key='-GET_TARGET-',
                                    font="meiryo")
                       ]
                   ], size=(500, 700), font="meiryo"
                   )


layout = [
    [
        frame11,
        frame21
    ]
]

window = sg.Window('gachasim', layout, resizable=True)

count = 0


def gacha_detail(val):
    res = []
    for i in range(val):
        random_int = int(random()*100000)
        target_int = int(float(values['-TAR_PER-']) * 1000)
        ssr_int = int(float(values['-SSR_PER-']) * 1000)
        sr_int = int(float(values['-SR_PER-']) * 1000)
        if 0 < random_int <= target_int:
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
        window['-RES_LOG-'].update(res)
        if '【' + values['-SSR-'] + '】' in res:
            window['-GET_TARGET-'].update(str(count) +
                                          '連で' + values['-NAME-'] + 'を入手')
        if count == 200:
            window['-GET_TARGET-'].update(str(count) +
                                          '連で' + values['-NAME-'] + 'を確定入手')


while True:
    event, values = window.read()

    if event is None:
        print('exit')
        break
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

    # frame1 button
    if event == '-ONE-':
        if (float(values['-SSR_PER-']) + float(values['-SR_PER-']) +
                float(values['-R_PER-'])) != 100:
            window['-ERROR-'].update('エラー:合計100%にしてください')
        else:
            count = count + 1
            gacha_detail(1)
            window['-COUNT-'].update(count)
    if event == '-TEN-':
        if (float(values['-SSR_PER-']) + float(values['-SR_PER-']) +
                float(values['-R_PER-'])) != 100:
            window['-ERROR-'].update('エラー:合計100%にしてください')
        else:
            count = count + 10
            gacha_detail(10)
            window['-COUNT-'].update(count)
    # default settings
    if event == '-DEFAULT-':
        window['-RARE-'].update('★★★')
        window['-SSR-'].update('★★★')
        window['-SR-'].update('★★')
        window['-R-'].update('★')
        window['-TAR_PER-'].update('0.750')
        window['-NAME-'].update('ミホノブルボン(バレンタイン)')
        window['-SSR_PER-'].update('3')
        window['-SR_PER-'].update('18')
        window['-R_PER-'].update('79')

    # frame2 button
    if event == '-ALL_CLEAR-':
        window['-ERROR-'].update('')
        window['-RES_LOG-'].update('')
        window['-GET_TARGET-'].update('')
        window['-COUNT-'].update('0')
        count = 0


window.close()

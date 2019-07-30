import QtQuick 2.10
import QtQuick.Controls 2.1
import QtQuick.Window 2.2
//import "func.js" as MyScript

ApplicationWindow {
    id: window
    visible: true

    property int w: 640
    property int h: 360

    // Window resolution
    width: w
    height: h

    property string word: "debug info"

    property int brdr: 0

    Text {
        id: text
        x: 0.5 * (parent.width - width)
        text: backend.text1
        font.italic: true
        font.pointSize: {
            (parent.width + parent.height) / 17
            //cpointSize(parent.width, parent.height, text.text.length)
        }
    }
	
    Text {
        id: debug
        color: "red"
        x: 0
        y: 0
        z: 100
        //text: backend.len2
        //text: backend.word
        //text: backend.red
        text: backend.text2
        visible: false
    }

    Text {
        id: counter
        color: "green"
        x: parent.width - 20
        y: 0
        z: 101
        text: backend.cur
        //anchors.left: window.right
    }

    Button {
        id: btn
        x: parent.width / 2 - btn.width / 2
        width: parent.width / 10
        height: parent.height / 15
        text: "<font color='#ffffff'>" + "Hint"
        font.family: "Arial"
        focus: true
        onClicked: {

            if (debug.visible) {
                debug.visible = false
                btn.text = "<font color='#ffffff'>" + "Hint"
            }
            else {
                debug.visible = true
                btn.text = "<font color='#000000'>" + "Hint"
            }
        }
    }

    Item {
    focus: true

    }

    Rectangle {
        id: rect
        width: parent.width * 0.8
        height: parent.height * 0.4
        x: 0.1 * width
        y: 0.5 * (parent.height - height)
        border.color: brdr ? "red" : "black"
        TextField {
            id: input
            width: parent.width
            height: parent.height
            //x: 0.5 * parent.width
            y: font.pointSize
            text: backend.word
            font.pointSize: (parent.width + parent.height) / 17
            maximumLength: backend.len2
            onTextChanged: {
                // Update variables and interface
                backend.word = input.text
                input.text = backend.word
                text.text = backend.text1
                // red border
                brdr = backend.red
                // text2 hint
                debug.text = backend.text2
                // current word hint
                counter.text = backend.cur
            }
            Keys.onPressed:
                if ((event.key == Qt.Key_F1))
                    if (debug.visible) {
                        debug.visible = false
                        btn.text = "<font color='#ffffff'>" + "Hint"
                    }
                    else {
                        debug.visible = true
                        btn.text = "<font color='#000000'>" + "Hint"
                    }

        }

    }
}



//function cpointSize(w, h, len) {
//    c = 0
//    if (len > 22) c = 24
//    else if (len > 18) c = 22
//    else if (len > 14) c = 20
//    else if (len > 10) c = 18
//    else if (len > 6) c = 16
//    return ((w + h) / c)
//}

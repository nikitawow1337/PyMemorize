import QtQuick 2.10
import QtQuick.Controls 2.1
import QtQuick.Window 2.2

ApplicationWindow {
    id: window
    visible: true

    property int w: 320
    property int h: 180

    // Window resolution
    width: w
    height: h

    property string word: "hello"

    property int cur: 0

    property var energy: backend.text.join();

    Text {
        id: text
        x: 0.5 * (parent.width - width)
        text: backend.text1
        font.italic: true
        font.pointSize: (parent.width + parent.height) / 17
    }
	
    Text {
        id: debug
        color: "red"
        x: 0
        y: 0
        z: 100
        //text: backend.len2
        text: backend.word
    }

    Rectangle {
        id: rect
        width: parent.width * 0.8
        height: parent.height * 0.4
        x: 0.1 * width
        y: 0.5 * (parent.height - height)
        border.color: backend.red ? "red" : "black"
        TextField {
            id: input
            width: parent.width
            height: parent.height
            //x: 0.5 * parent.width
            y: font.pointSize
            text: backend.word
            font.pointSize: (parent.width + parent.height) / 15
            //maximumLength: backend.len2
            onTextChanged: {
                backend.word = input.text
                input.text = backend.word
                text.text = backend.text1
                //text.text = backend.text1
                //backend.cur += 1
                //cur += 1
            }
        }
    }
}

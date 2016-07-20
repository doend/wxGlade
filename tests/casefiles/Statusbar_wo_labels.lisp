#!/usr/bin/env lisp
;;;
;;; generated by wxGlade "faked test version"
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxCL)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFrame)
(use-package :wxSizer)
(use-package :wxStaticText)
(use-package :wxStatusBar)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; end wxGlade


(defclass MyFrame()
        ((top-window :initform nil :accessor slot-top-window)
        (label-1 :initform nil :accessor slot-label-1)
        (sizer-1 :initform nil :accessor slot-sizer-1)
        (statusbar-without-labels :initform nil :accessor slot-statusbar-without-labels)))

(defun make-MyFrame ()
        (let ((obj (make-instance 'MyFrame)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj MyFrame))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: MyFrame.__init__
        (setf (slot-label-1 obj) (wxStaticText_Create (slot-top-window obj) wxID_ANY (_"Example of a statusbar with three fields\nbut without labels in those fields.") -1 -1 -1 -1 0))
        (setf (slot-statusbar-without-labels obj) (wxFrame_CreateStatusBar (slot-top-window obj) 3 0))
        ;;; end wxGlade
        )

(defmethod set-properties ((obj MyFrame))
        ;;; begin wxGlade: MyFrame.__set_properties
        (wxFrame_SetTitle (slot-top-window obj) (_"frame_1"))
        (wxStatusBar_SetStatusWidths (slot-statusbar-without-labels obj) 3 (vector -1 -1 -1))
        ;;; end wxGlade
        )

(defmethod do-layout ((obj MyFrame))
        ;;; begin wxGlade: MyFrame.__do_layout
        (setf (slot-sizer-1 obj) (wxBoxSizer_Create wxVERTICAL))
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-label-1 obj) 1 (logior wxALL wxEXPAND) 5 nil)
        (wxWindow_SetSizer (slot-top-window obj) (slot-sizer-1 obj))
        (wxSizer_Fit (slot-sizer-1 obj) (slot-top-window obj))
        (wxFrame_layout (slot-frame-1 self))
        ;;; end wxGlade
        )

;;; end of class MyFrame



;(function() {

    jsPlumb.ready(function() {

        // list of possible anchor locations for the blue source element
        var sourceAnchors = [
            [ 0, 1, 0, 1 ],
            [ 0.25, 1, 0, 1 ],
            [ 0.5, 1, 0, 1 ],
            [ 0.75, 1, 0, 1 ],
            [ 1, 1, 0, 1 ]
        ];

        var instance = jsPlumb.getInstance({
            // set default anchors.  the 'connect' calls below will pick these up, and in fact setting these means
            // that you also do not need to supply anchor definitions to the makeSource or makeTarget functions.
            Anchors : [ sourceAnchors, "TopCenter" ],
            // drag options
            DragOptions : { cursor: "pointer", zIndex:2000 },
            // default to blue at source and green at target
            EndpointStyles : [{ fillStyle:"#0d78bc" }, { fillStyle:"#558822" }],
            // blue endpoints 7 px; green endpoints 11.
            Endpoints : [ ["Dot", { radius:7 } ], [ "Dot", { radius:11 } ] ],
            // default to a gradient stroke from blue to green.  for IE provide all green fallback.
            PaintStyle : {
                gradient:{ stops:[ [ 0, "#0d78bc" ], [ 1, "#558822" ] ] },
                strokeStyle:"#558822",
                lineWidth:10
            },
            Container:"source-target-demo"
        });

        /*
        // click listener for the enable/disable link.
        jsPlumb.CurrentLibrary.bind(document.getElementById("enableDisableSource"), "click", function(e) {
            var state = instance.toggleSourceEnabled("sourceWindow1");
            this.innerHTML = (state ? "disable" : "enable");
            e.stopPropagation();
            e.preventDefault();
        });
        */
        // bind to a connection event, just for the purposes of pointing out that it can be done.
        instance.bind("connection", function(i,c) {
            console.dir(i.connection);
        });

        // get the list of ".smallWindow" elements.
        var smallWindows = jsPlumb.getSelector(".smallWindow");
        // make them draggable
        //instance.draggable(smallWindows);
        smallWindows.draggable({
            drag: function() {
                var cookie = JSON.stringify($(this).offset());
                $.cookie($(this).attr('id') + '_pos', cookie, { expires: 365 });
            }
        });

        $(".smallWindow").each(function() {
            try {
                var cookie =  $.cookie($(this).attr('id') + '_pos');
                var pos = JSON.parse(cookie);

                $(this).offset(pos);
            } catch(e) {
            }
        });
        // suspend drawing and initialise.
        instance.doWhileSuspended(function() {

            // configure the .smallWindows as targets.
            instance.makeTarget(smallWindows, {
                //anchor:"TopCenter",               // you could supply this if you want, but it was set in the defaults above.
                dropOptions:{ hoverClass:"hover" },
                uniqueEndpoint:true
            });

            // and finally connect a couple of small windows, just so its obvious what's going on when this demo loads.
            instance.connect({ source:"sourceWindow1", target:"targetWindow5" });
            instance.connect({ source:"sourceWindow1", target:"targetWindow2" });
        });
    });
})();
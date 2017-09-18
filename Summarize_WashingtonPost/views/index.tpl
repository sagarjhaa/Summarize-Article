% rebase('layout.tpl', title='Home Page', year=year)


<br />
<br />
<form action="/summarize" method="post" class="form-inline">
    <div class="row">
        <div class="form-group col-md-7" >
            <input name="articleURL" class="form-control " style="max-width:100%" type="url" required placeholder="Washington post article url"/>
        </div>

        <div class="form-group col-md-3">
            <input name="noOfLines" class="form-control" type="number" placeholder="Lines in summary"/>
        </div>

        <div class="form-group col-md-2">
            <input id="submit" type="Submit" class="btn btn-default" value="Summarize" />
        </div>

    </div>
</form>

<br />
<br />
<br />
<div class="container">
    <div class="row">
        <div class="col-md-6">
            <div class="panel panel-default" style="max-height:75vh;overflow:scroll">
                <div class="panel-heading">
                    <h3 class="panel-title">Original article</h3>
                </div>
                <div class="panel-body">
                    {{OriginalText}}
                </div>
            </div>
        </div>

        <div class="col-md-6">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">Summary article</h3>
                </div>
                <div class="panel-body">
                    {{Summary}}
                </div>
            </div>
        </div>
    </div>
</div>
<!--<script>
    $("#submit").submit(function (d) {
        e.preventDefault();
        alert("sagar jha");
    });
</script>-->


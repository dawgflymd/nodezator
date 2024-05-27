""""""

from ...config import APP_REFS

from ...our3rdlibs.behaviour import indicate_unsaved


def update_with_widget(data, key, widget):
    """Update data's key with value from widget.

    Parameters
    ==========
    data (dict)
        dict whose given key is to be updated.
    key (string)
        key to be update.
    widget (custom Python class)
        use its 'get' method to retrieve the value.
    """
    ### check whether changes in data must be indicated

    ## get current and new value

    current = data[key]
    new = widget.get()

    ## if the new value has the same value and type of the current one,
    ## return earlier

    if (
        new == current
        and (type(new) is type(current))
    ):
        return

    ### otherwise update the value in the data and indicate
    ### that the data was changed

    data[key] = widget.get()
    indicate_unsaved()

    ### also indicate birdseye view state of window manager must
    ### have its objects updated next time it is set
    APP_REFS.ea.must_update_birdseye_view_objects = True

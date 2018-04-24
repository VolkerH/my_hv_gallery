import pandas as pd

def well_nr_to_coords(nr, nx=12, ny=8):
    """Converts well_nr_to well coordinates. 
    To be used with pandas dataframes that have a wellnumber column like this:
    
    wellcoords = df.well.apply(well_nr_to_coords)
    df = pd.concat([df, wellcoords],axis=1)
    """
    
    cols = [nx] + [i+1 for i in range(nx-1)]
    rows = [chr(i+ord('A')) for i in range(ny)]
    
    colindex = nr  % nx   
    rowindex = int((nr-1) / nx)   
    return pd.Series(dict(row=rows[rowindex], col=cols[colindex], rownum=rowindex))

def create_custom_tooltip(info_fields, impath, im_col_name, height=200, width=200):
    """ Generates a custom HTML string for a tooltip
    info_fields: list of columnnames specifying the columns which should be displayed in the tooltip
    impath: path where the images to include in the tooltips are located (string)
    im_col_name: column name that contains the names of the images to include in the tooltip (string)
    height: integer specifying image height
    width: integer ...
    """
    info_html = ""
    for colnames in info_fields:
        info_html += f"""
            <div>
                <span style="font-size: 15px;">{colnames} @{colnames} </span>
            </div>"""

    custom_ttip = f"""
    <div>
        <div>
            <img
                src="@{im_col_name}" height="{height}" width="{width}"
                style="float: left; margin: 0px 15px 15px 0px;"
                border="2"
            ></img>
        </div>
        {info_html}
    </div>
    """
    return custom_ttip
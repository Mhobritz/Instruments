function ImageTypeSelector({imageType, setImageType}) {

    function GetImageTypeClicked(e) {
        setImageType(e.target.value)
    }
    
  return (
    <fieldset> 
        <legend>
            Image Type
        </legend>
        <label> Bias
            <input type='radio' name='ExpType' onChange={GetImageTypeClicked} value='Bias'
            checked={
                imageType === 'Bias'
            }/>
        </label>
        <label> Flat
            <input type='radio' name='ExpType' onChange={GetImageTypeClicked} value='Flat'
            checked={
                imageType === 'Flat'
            }/>
        </label>
        <label> Dark
            <input type='radio' name='ExpType' onChange={GetImageTypeClicked} value='Dark'
            checked={
                imageType === 'Dark'
            }/>
        </label>
        <label> Object
            <input type='radio' name='ExpType' onChange={GetImageTypeClicked} value='Object'
            checked={
                imageType === 'Object'
            }/>
        </label>
    </fieldset>
  );
}



export default ImageTypeSelector;

# Querying the Property Database

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/propdb-queries/

---

# Querying the Property Database

The [Property Database](/en/docs/viewer/v7/reference/globals/PropertyDatabase) contains all of the BIM data for a construction model and the manufacturing data for manufacturing models. The Property Database is kept on a dedicated [web worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) and accessing it is done via asynchronous messages.

In this example weâll be writing a function that queries the Property Database of the model directly inside the web worker execution context.

## [Step 1: Writing a custom query function](#step-1-writing-a-custom-query-function)

Letâs start by writing a trivial query function for the Property Database.

```
function userFunction(pdb) {
    return 42;
}

```

The trivial query function doesnât interact with `pdb`, the Property Database, yet. Weâll implement rhw interaction in Step 3. For now weâll have it return a fixed value of `42`.

## [Step 2: Executing the custom query function](#step-2-executing-the-custom-query-function)

Use `viewer.model.getPropertyDb().executeUserFunction(userFunction)` which returns a `Promise` that resolves with the return value of `userFunction`.

```
var thePromise = viewer.model.getPropertyDb().executeUserFunction( userFunction );
thePromise.then(function(retValue){
    console.log('retValue is: ', retValue); // prints 'retValue is: 42'
}).catch(function(err){
  console.log("Something didn't go right...")
  console.log(err);
});

```

After executing this code snippet, youâll see the message **retValue is: 42** in the browserâs developer console.

## [Step 3: Querying the Property Database](#step-3-querying-the-property-database)

Now itâs time to modify our `userFunction` to have it interact with the Property Database.

The objective of the custom query function is to return the ids of the heaviest parts in the model. To do this, weâll iterate over all part-ids in the model and check their *Mass* property value.

Due to the Property Database data layout, weâll first need to identify the index for the âMassâ property.
Update the custom query function as follows:

```
function userFunction(pdb) {

    //return 42;

    var attrIdMass = -1;

    // Iterate over all attributes and find the index to the one we are interested in
    pdb.enumAttributes(function(i, attrDef, attrRaw){

        var name = attrDef.name;

        if (name === 'Mass') {
            attrIdMass = i;
            return true; // to stop iterating over the remaining attributes.
        }
    });
}

```

Show More

If the value of `attrIdMass` is different than `-1`, then we know that the modelâs Property Database contains âMassâ data for its parts. Next weâll have the function iterate over all parts and their properties, to find out which one is the largest.

```
function userFunction(pdb) {

    //return 42;

    var attrIdMass = -1;

    // Iterate over all attributes and find the index to the one we are interested in
    pdb.enumAttributes(function(i, attrDef, attrRaw){

        var name = attrDef.name;

        if (name === 'Mass') {
            attrIdMass = i;
            return true; // to stop iterating over the remaining attributes.
        }
    });

    // Early return is the model doesn't contain data for "Mass".
    if (attrIdMass === -1)
      return null;

    // Now iterate over all parts to find out which one is the largest.
    var maxValue = 0;
    var maxValId = -1;
    pdb.enumObjects(function(dbId){

        // For each part, iterate over their properties.
        pdb.enumObjectProperties(dbId, function(attrId, valId){

            // Only process 'Mass' property.
            // The word "Property" and "Attribute" are used interchangeably.
            if (attrId === attrIdMass) {

                var value = pdb.getAttrValue(attrId, valId);

                if (value > maxValue) {
                    maxValue = value;
                    maxValId = dbId;
                }

                // Stop iterating over additional properties when "Mass" is found.
                return true;
            }
        });
    });

    // Return results
    return {
      id: maxValId,
      mass: maxValue
    }
}

```

Show More

And finally, the Promiseâs `resolve` function from Step 2 will have to be updated, too. In this case, weâll have the viewer select and focus (zoom) on the largest part.

```
var thePromise = viewer.model.getPropertyDb().executeUserFunction( userFunction );
thePromise.then(function(retValue){

    //if (retValue === 42) {
    //  console.log('We got the expected value back.');
    //}

    if (!retValue) {
      console.log("Model doesn't contain property 'Mass'.");
      return;
    }

    var mostMassiveId = retValue.id;
    viewer.select(mostMassiveId);
    viewer.fitToView([mostMassiveId]);
    console.log('Most massive part is', mostMassiveId, 'with Mass:', retValue.mass);
});

```

Show More

## [Final thoughts](#final-thoughts)

When writing your own `userFunction`, make sure that you avoid referencing objects that live outside the functionâs scope. This is because the function gets serialized when messaged to the web worker.

## [Whatâs next?](#what-s-next)

To view an interactive example, see [Querying Model Properties](/en/docs/viewer/v7/developers_guide/interactive_examples/example_3/).

See [Property Database](/en/docs/viewer/v7/reference/globals/PropertyDatabase) for the instance methods available for your custom query function.

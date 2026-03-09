# Task 4 â Display the Model in the Viewer

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-file4viewer/task4-display_model/

---

# Task 4 â Display the Model in the Viewer

To display the SVF2 file you generated, you can create an HTML page and embed the source file URN in it (Option 1 below). Alternatively, you enter the source file URN in an HTML page we have already created for you (Option 2).

## [Option 1: Embed the Source File URN in an HTML Page](#option-1-embed-the-source-file-urn-in-an-html-page)

1. Insert an instance of the Viewer in an HTML page, and initialize it as per the instructions provided in the [Viewer Basics topic in the Viewer SDK documentation:](../../viewer/developers-guide-docs/viewer_basics-starting-html.md)

> | Parameter | SVF2 |
> | --- | --- |
> | `api` | streamingV2 |
> | `env` | AutodeskProduction2 |

2. Take the URL safe Base64-encoded URN of the source file, which you obtained in the previous task, and embed it as described in the section [Load a Model](../../viewer/developers-guide-docs/viewer_basics-starting-html.md#id3) in the topic [Getting Started](../../viewer/developers-guide-docs/viewer_basics-starting-html.md).
> **Note:** Add `urn:` to the URL safe Base64-encoded URN, when you embed it in the JavaScript code, as show in the following image.
>
> 

## [Option 2: Enter the Source File URN on an existing HTML page](#option-2-enter-the-source-file-urn-on-an-existing-html-page)

We have created a web page based on the instructions provided in Option 1. You can use it to verify the SVF2 file you just generated.

1. Display the webpage for SVF2 by clicking the link in the following table:

> | SVF2 |
> | --- |
> | [Show Web page](https://autodesk-platform-services.github.io/aps-tutorial-postman/display_svf2.html) |
> |  |
> | [Source](https://github.com/autodesk-platform-services/aps-tutorial-postman/blob/master/docs/display_svf2.html) |

1. In the **Access Token** box, specify the access token you obtained in Task 1 of this tutorial.

2. In the **Source File URN (encoded)** box, specify the URL safe Base64-encoded URN of the source file, which you noted down in the previous task.

3. Click **Submit**.
    You should see a screen similar to the following.



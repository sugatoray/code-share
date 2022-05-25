# Using Better Comments and Color Picker/Info

We often use comments to write explanation of what we are doing in a document.
But if there were a way to separately highlight the comments, that would have been nice right?

Well, there is a way: you can use the VS Code extension `Better Comments`.

![better-comments-example][#better-comments-example]


[#better-comments-example]: better_comments_example.png

## Better Comments Schema

```json
{
        "better-comments.tags": [
        {
            "tag": "!",
            "color": "#FF2D00",
            "strikethrough": false,
            "bold": false,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
        {
            "tag": "?",
            "color": "#3498DB",
            "strikethrough": false,
            "bold": false,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
        {
            "tag": "//",
            "color": "#474747",
            "strikethrough": true,
            "bold": false,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
        {
            "tag": "todo",
            "color": "#FF8C00",
            "strikethrough": false,
            "bold": false,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
        {
            "tag": "*",
            "color": "#98C379",
            "strikethrough": false,
            "bold": false,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
        // User Defined
        {
            "tag": "**",
            "color": "#98C379",
            "strikethrough": false,
            "bold": true,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
        // User Defined
        {
            "tag": "_",
            "color": "#98C379",
            "strikethrough": false,
            "bold": false,
            "italic": true,
            "underline": false,
            "backgroundColor": "transparent"
        },
        // User Defined
        {
            "tag": "@@",
            "color": "#E5FF00",
            "strikethrough": false,
            "bold": true,
            "italic": false,
            "underline": false,
            "backgroundColor": "transparent"
        },
    ],
}
```

<details>

<summary>
    <strong>Click to see figure</strong>
</summary>

<p>

![better-comments-schema][#better-comments-schema]

[#better-comments-schema]: better_comments_schema.png

</p>
</details>

## Color Picker/Info: VS Code Extensions

The `css` file is used to pick colors.

![color-info-extension][#color-info-extension]

[#color-info-extension]: color_info_screenshot.png

![color-picker-extension][#color-picker-extension]

[#color-picker-extension]: color_picker_screenshot.png

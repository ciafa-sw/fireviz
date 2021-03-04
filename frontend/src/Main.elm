module Main exposing (main)

{--
config for FIREFRONT firebase project


<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/8.2.9/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->

<script>
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyBBlBR8rh89FhiiyCUsuiAVziqUZd2pb3k",
    authDomain: "firefront-1ce0d.firebaseapp.com",
    projectId: "firefront-1ce0d",
    storageBucket: "firefront-1ce0d.appspot.com",
    messagingSenderId: "109035253303",
    appId: "1:109035253303:web:79229e432a1fa7b30159b2"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
</script>
--}

import Browser exposing (Document)
import Browser.Navigation as Nav

import Url exposing (Url)
import Url.Parser as Parser exposing ((</>), Parser, s, string)
import Url.Builder as Builder


import Json.Decode as Dec
--import Json.Decode.Pipeline exposing (optional, required)
import Json.Encode as Enc

import Element as E exposing (Element, el, text, column, row, alignRight, fill, width, rgb255, spacing, centerY, padding)
import Element.Background as Background
import Element.Border as Border
import Element.Font as Font
import Element.Input as Input

import Html


-- Model

type alias Model =
    { key : Nav.Key
    , page : Page
    }

type Page
    = FireVisorPage
    | NotFound


type Route
    = FireVisor


type Msg
    = ClickedLink Browser.UrlRequest
    | ChangedUrl Url


update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        ClickedLink urlRequest ->
            case urlRequest of
                Browser.External href ->
                    ( model, Nav.load href )  -- Nav.load -> full page load

                Browser.Internal url ->
                    ( model, Nav.pushUrl model.key (Url.toString url) )

        ChangedUrl url ->
            updateUrl url model

-- View

view : Model -> Document Msg
view model =
    { title = "What's for lunch?"
    , body =
          [ content model
          ]
    }


content : Model -> Html.Html Msg
content model =
    case model.page of
        FireVisorPage ->
            fireVisorView model
                |> appView
        NotFound ->
            notFoundView


notFoundView : Html.Html Msg
notFoundView  = 
    E.layout
        [ E.width E.fill
        , E.height E.fill
        ] <|
        E.el
            [ E.centerX
            , E.centerY
            ]
            (text "Uops! Page not found!")



appView : E.Element Msg -> Html.Html Msg
appView pageRendered = 
    E.layout
        [ E.width E.fill
        , E.height E.fill
        ] <|
        E.column
            []
            [ configHeader
            , E.row
                []
                [ sideBar
                , pageRendered
                ]
            ]

sideBar : E.Element Msg
sideBar =
    let
        linkRouter : String -> String -> E.Element Msg
        linkRouter label url = 
            E.link
                [ Border.dashed ]
                { url = url
                , label = text label
                }

    in
        E.column
            [ E.spacing 10
            , E.padding 10
            ]
            [ linkRouter "some link" "/some/path"
            ]


fireVisorView : Model -> E.Element Msg
fireVisorView model =
        E.column
            [ E.padding 10
            , E.spacing 20
            , Border.dashed
            , Border.rounded 10
            ]
            [ E.column
                [ E.centerX
                , E.centerY
                    , E.spacing 10
                ]
                [ text "operation data"
                ]
            ]

configHeader : E.Element Msg
configHeader =
    -- TODO add FIREFRONT logo
    E.row
        [ E.width E.fill
        , E.centerX ]
        [ E.el
            [ Font.size 50
            , E.alignLeft
            , E.padding 20
            ] (text <| "FIREFRONT | FireVisor")
        ]


main : Program () Model Msg
main =
    Browser.application
        { init = init
        , subscriptions = subscriptions
        , update = update
        , view = view
        , onUrlRequest = ClickedLink
        , onUrlChange = ChangedUrl
        }

subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none
    {--Sub.batch
        [ authUpdate (Dec.decodeValue (Dec.nullable userAuthDecoder) >> AuthUpdate)
        , gotUserData (Dec.decodeValue (Dec.nullable userDataDecoder) >> GotUserData)
        ]
    --}

init : () -> Url -> Nav.Key -> (Model, Cmd Msg) -- first argument is flags
init () url key =
    updateUrl url
        { key = key
        , page = FireVisorPage
        }
            |> Debug.log "init main:" 


updateUrl : Url -> Model -> (Model, Cmd Msg)
updateUrl url model =
    case Parser.parse parser url of
        Just FireVisor ->
            ( { model | page = FireVisorPage }, Cmd.none )
            
        Nothing ->
            ( { model | page = NotFound }, Cmd.none )

parser : Parser (Route -> a) a
parser =
    Parser.oneOf
        [ Parser.map FireVisor Parser.top
        ]
{{ with secret "pki/internal/issue/consul" "common_name=consul.service.consul" }}
{{ .Data.issuing_ca }}{{- end -}}
